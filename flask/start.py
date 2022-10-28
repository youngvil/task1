import os

from collections import namedtuple

from flask import Flask, render_template

app = Flask(__name__)
Limit = namedtuple('Limit', 'text tag')
limits = []


def collect_cpu_max(path, file):
    x = path + file
    file = open(x, 'r')
    text = file.readline()
    cpu_max = int(text.split(' ')[0])
    period = int(text.split(' ')[1])
    cpu_max_perc = cpu_max / period * 100
    file.close()
    line = str(cpu_max_perc) + " %"
    return line


def collect_memory_max(path, file):
    x = path + file
    file = open(x, 'r')
    text = file.readline()
    memory_max = int(text) / pow(2, 20)
    file.close()
    line = str(memory_max) + 'MB'
    return line


def get_limits():
    path = '/sys/fs/cgroup/'
    stats = ['cpu.max', 'memory.max']
    limits.append(Limit(collect_cpu_max(path, stats[0]), stats[0]))
    limits.append(Limit(collect_memory_max(path, stats[1]), stats[1]))
    return limits


@app.route("/", methods=['GET'])
def hello_world():
    return render_template('index.html', limits=get_limits())


# @app.route('/main', methods=['GET'])
# def main():
#    return render_template('main.html', limits=limits_data)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
