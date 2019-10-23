@app.route('/add')
def addition():
    result = 0
    for arg in request.args:
        try:
            result = result + eval(request.args.get(arg, default="0"))
        except:
            pass
    return '%f \n' % result
