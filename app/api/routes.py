from app.api import bp
from app.models import User

@bp.route('/users', methods=['GET'])
def get_users():
    return User.objects.all().to_json()