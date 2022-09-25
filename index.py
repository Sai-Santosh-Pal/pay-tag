from flask import Flask, jsonify
app = Flask(__name__)

import scratchconnect

@app.route('/')
def balance():
    user = scratchconnect.ScratchConnect("SaiSantoshPal", "sai2010**")
    project = user.connect_project(project_id=733246147)
    variables = project.connect_cloud_variables()
    variables.get_variable_data(limit=100, offset=0)  # Returns the cloud variable data
    balance = variables.get_cloud_variable_value(variable_name="balance", limit=100)
    balance_dict = {
        "balance": balance[0]
    }
    return jsonify(balance_dict) 

@app.route('/add_balance/<int:amount>/')
def add_balance(amount):
    user = scratchconnect.ScratchConnect("SaiSantoshPal", "sai2010**")
    project = user.connect_project(project_id=733246147)
    variables = project.connect_cloud_variables()
    variables.get_variable_data(limit=100, offset=0)
    balancese = variables.get_cloud_variable_value(variable_name="balance", limit=100)
    set = variables.set_cloud_variable(variable_name="balance", value=amount + int(balancese[0]))
    balancese = variables.get_cloud_variable_value(variable_name="balance", limit=100) 
    # write_history(typeOf="add", add=amount)
    balance_dict = {
        "balance": balancese[0]
    }
    return jsonify(balance_dict) 

@app.route('/sub_balance/<int:amount>/')
def sub_balance(amount):
    user = scratchconnect.ScratchConnect("SaiSantoshPal", "sai2010**")
    project = user.connect_project(project_id=733246147)
    variables = project.connect_cloud_variables()
    variables.get_variable_data(limit=100, offset=0)
    balancese = variables.get_cloud_variable_value(variable_name="balance", limit=100)
    set = variables.set_cloud_variable(variable_name="balance", value=int(balancese[0])-amount)
    balancese = variables.get_cloud_variable_value(variable_name="balance", limit=100) 
    # write_history(typeOf="sub", sub=amount)
    balance_dict = {
        "balance": balancese[0]
    }
    return jsonify(balance_dict)


@app.route('/sub_balance_petrol/<int:amount>/')
def sub_balance_petrol(amount):
    try:
        user = scratchconnect.ScratchConnect("SaiSantoshPal", "sai2010**")
        project = user.connect_project(project_id=733246147)
        variables = project.connect_cloud_variables()
        variables.get_variable_data(limit=100, offset=0)
        balancese = variables.get_cloud_variable_value(variable_name="balance", limit=100)
        set = variables.set_cloud_variable(variable_name="balance", value=int(balancese[0])-amount)
        balancese = variables.get_cloud_variable_value(variable_name="balance", limit=100) 
        # write_history(typeOf="subp", sub=amount)
        message = {
        "msg": f"Successfull paid {amount}P!"
        }
        return jsonify(message)
        
    except Exception:
        message = {
        "msg": "Transaction failed"
        }
        return jsonify(message)

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')
