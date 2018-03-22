from flask import Blueprint
from bear import PARAMETRIC_ABUNDANCE

bp = Blueprint('simulators', __name__)

SIMULATORS = {
    'bear.parametric_abundance': PARAMETRIC_ABUNDANCE
}

def to_json():
    result = {}
    for key in SIMULATORS:
        name, subname = key.split('.')
        if name not in result:
            result[name] = {}

        result[name][subname] = SIMULATORS[key]
    return result

from app.simulators import routes