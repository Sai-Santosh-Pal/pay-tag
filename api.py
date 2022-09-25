from flask import Flask
app = Flask(__name__)

import scratchconnect




    
# user = scratchconnect.ScratchConnect("SaiSantoshPal", "sai2010**")
# project = user.connect_project(project_id=733246147)
# variables = project.connect_cloud_variables()
# variables.get_variable_data(limit=100, offset=0)  # Returns the cloud variable data
# balance = variables.get_cloud_variable_value(variable_name="balance", limit=100)
# balances = balance[0]
@app.route('/balance/')
def balance():
    user = scratchconnect.ScratchConnect("SaiSantoshPal", "sai2010**")
    project = user.connect_project(project_id=733246147)
    variables = project.connect_cloud_variables()
    variables.get_variable_data(limit=100, offset=0)  # Returns the cloud variable data
    balance = variables.get_cloud_variable_value(variable_name="balance", limit=100)
    balances = balance[0]
    return balances

@app.route(f'/add_balance/<int:amount>/')
def add_balance(amount):
    # user = scratchconnect.ScratchConnect("SaiSantoshPal", "sai2010**")
    # project = user.connect_project(project_id=733246147)
    # variables = project.connect_cloud_variables()
    # variables.get_variable_data(limit=100, offset=0)  # Returns the cloud variable data
    # balance = variables.get_cloud_variable_value(variable_name="balance", limit=100)
    # balances = balance[0]
    user = scratchconnect.ScratchConnect("SaiSantoshPal", "sai2010**")
    project = user.connect_project(project_id=733246147)
    variables = project.connect_cloud_variables()
    variables.get_variable_data(limit=100, offset=0)
    balancese = variables.get_cloud_variable_value(variable_name="balance", limit=100)
    set = variables.set_cloud_variable(variable_name="balance", value=amount + int(balancese[0]))
    balancese = variables.get_cloud_variable_value(variable_name="balance", limit=100) 
    # write_history(typeOf="add", add=amount)
    return balancese[0]

@app.route(f'/sub_balance/<int:amount>/')
def sub_balance(amount):
    # user = scratchconnect.ScratchConnect("SaiSantoshPal", "sai2010**")
    # project = user.connect_project(project_id=733246147)
    # variables = project.connect_cloud_variables()
    # variables.get_variable_data(limit=100, offset=0)  # Returns the cloud variable data
    # balance = variables.get_cloud_variable_value(variable_name="balance", limit=100)
    # balances = balance[0]
    user = scratchconnect.ScratchConnect("SaiSantoshPal", "sai2010**")
    project = user.connect_project(project_id=733246147)
    variables = project.connect_cloud_variables()
    variables.get_variable_data(limit=100, offset=0)
    balancese = variables.get_cloud_variable_value(variable_name="balance", limit=100)
    set = variables.set_cloud_variable(variable_name="balance", value=int(balancese[0])-amount)
    balancese = variables.get_cloud_variable_value(variable_name="balance", limit=100) 
    # write_history(typeOf="sub", sub=amount)
    return balancese[0]

@app.route(f'/sub_balance_petrol/<int:amount>/')
def sub_balance_petrol(amount):
    # user = scratchconnect.ScratchConnect("SaiSantoshPal", "sai2010**")
    # project = user.connect_project(project_id=733246147)
    # variables = project.connect_cloud_variables()
    # variables.get_variable_data(limit=100, offset=0)  # Returns the cloud variable data
    # balance = variables.get_cloud_variable_value(variable_name="balance", limit=100)
    # balances = balance[0]
    try:
        user = scratchconnect.ScratchConnect("SaiSantoshPal", "sai2010**")
        project = user.connect_project(project_id=733246147)
        variables = project.connect_cloud_variables()
        variables.get_variable_data(limit=100, offset=0)
        balancese = variables.get_cloud_variable_value(variable_name="balance", limit=100)
        set = variables.set_cloud_variable(variable_name="balance", value=int(balancese[0])-amount)
        balancese = variables.get_cloud_variable_value(variable_name="balance", limit=100) 
        # write_history(typeOf="subp", sub=amount)
        return f"Successfull paid {amount}P!"
    except Exception:
        return "Transaction failed"

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')
