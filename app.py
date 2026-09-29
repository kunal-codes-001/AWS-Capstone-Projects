from flask import Flask, render_template
import urllib.request

app = Flask(__name__)


def get_metadata(path):
    token_request = urllib.request.Request(
        "http://169.254.169.254/latest/api/token",
        method="PUT",
        headers={
            "X-aws-ec2-metadata-token-ttl-seconds": "21600"
        }
    )

    token = urllib.request.urlopen(token_request).read().decode()

    request = urllib.request.Request(
        f"http://169.254.169.254/latest/meta-data/{path}",
        headers={
            "X-aws-ec2-metadata-token": token
        }
    )

    return urllib.request.urlopen(request).read().decode()


@app.route("/")
def home():
    instance_id = get_metadata("instance-id")
    hostname = get_metadata("hostname")
    availability_zone = get_metadata("placement/availability-zone")

    return render_template(
        "index.html",
        instance_id=instance_id,
        hostname=hostname,
        availability_zone=availability_zone
    )


app.run(host="0.0.0.0", port=5000)
