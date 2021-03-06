from flask import Flask
from flask import render_template
from search import search
from flask import *
import os



app = Flask(__name__)


@app.route('/')
def first():
    return render_template('main.html')#predict.html
@app.route('/search')
def sear():
    return render_template('search.html')

@app.route('/req1', methods=['POST'])
def req1():
    inp =  request.form['inp'];
    if(len(inp)>0):
        res=search(inp.strip())
        # out= json.dumps({'status':'OK','name':res[0],'address':res[1],'camp':res[2]});
        out=res.to_json()
        print(out)

        return  out
    else:
        print("no inp")
    return json.dumps({'status':'OK','name':'','address':'','camp':''});
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')
@app.route('/register')
def second():
    return render_template('register.html')


@app.route("/upload", methods=["POST"])
def upload():
    """Handle the upload of a file."""
    form = request.form

    # Create a unique "session ID" for this particular batch of uploads.
    # upload_key = str(uuid4())

    # Is the upload using Ajax, or a direct POST by the form?
    is_ajax = False
    if form.get("__ajax", None) == "true":
        is_ajax = True


    print("=== Form Data ===")
    details = list()
    for key, value in list(form.items()):
        details.append(value)
    f = open("../data/details.csv", "a")
    #print(details[3].replace('\r',"").replace('\n',","))
    f.write("\n0\t" + details[0].strip()   + "\t" + details[3].strip().replace('\r',"").replace('\n',",")+ "\t" + details[2].strip().replace('\r',"").replace('\n',",") + "\t" + details[1].strip())#additional message removed
    f.close()

    return redirect(url_for("upload"))


@app.route('/upload')
def upload_complete():
    return render_template(
        'main.html')  # abin shoby change your search python code so that it ll able to search for the input name and return

@app.route('/setreq', methods=['POST'])
def setreq():

    data=[]
    data.append(request.form['items'])

    data.append( request.form['quantity'])

    data.append( request.form['campName'])

    data.append(request.form['district'])

    data.append(request.form['userName'])

    #variable = tot_req1["dataArr"]
    print(data)
    if(data[0]==""or data[1]==""or data[2]==""or data[3]==""or data[4]==""):
        return '201'
    else:
        f = open("../data/requirements.csv", "a")
        # print(details[3].replace('\r',"").replace('\n',","))
        f.write("\n" + data[0].strip() + "\t" + data[3].strip().replace('\r', "").replace('\n', ",") + "\t" +
                data[2].strip().replace('\r', "").replace('\n', ",") + "\t" + data[
                    1].strip())  # additional message removed
        f.close()
        return '200'
    return '201'
@app.route('/request')
def reqt():
    return render_template(
        'require.html')

if __name__ == '__main__':
    app.run(debug=True)