from flask import Flask, render_template, request, jsonify, Response
from flask_httpauth import HTTPBasicAuth
from kubernetes import client, config
from functools import wraps
import os

app = Flask(__name__)
auth = HTTPBasicAuth()

# Kullanıcı adı ve şifre ortam değişkenlerinden alınır
USERNAME = os.getenv("APP_USER", "admin")
PASSWORD = os.getenv("APP_PASSWORD", "password")

# Kubernetes API yapılandırması
def kube_config():
    try:
        config.load_incluster_config()
    except:
        config.load_kube_config()

v1 = client.CoreV1Api()

# Kimlik doğrulama kontrol fonksiyonu
def check_auth(username, password):
    return username == USERNAME and password == PASSWORD

def authenticate():
    return Response(
        'Giriş yapmanız gerekiyor.', 401,
        {'WWW-Authenticate': 'Basic realm="Login Required"'}
    )

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated

@app.route('/')
@requires_auth
def index():
    namespaces = [ns.metadata.name for ns in v1.list_namespace().items]
    return render_template('index.html', namespaces=namespaces)

@app.route('/namespaces', methods=['GET'])
@requires_auth
def list_namespaces():
    namespaces = [ns.metadata.name for ns in v1.list_namespace().items]
    return jsonify(namespaces)

@app.route('/pods/<namespace>', methods=['GET'])
@requires_auth
def list_pods(namespace):
    pods = v1.list_namespaced_pod(namespace)
    pod_names = [pod.metadata.name for pod in pods.items]
    return jsonify(pod_names)

@app.route('/logs/<namespace>/<pod>', methods=['GET'])
@requires_auth
def get_logs(namespace, pod):
    container_name = request.args.get('container', None)
    try:
        if container_name:
            logs = v1.read_namespaced_pod_log(name=pod, namespace=namespace, container=container_name)
        else:
            logs = v1.read_namespaced_pod_log(name=pod, namespace=namespace)
        return jsonify({'logs': logs})
    except client.exceptions.ApiException as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)