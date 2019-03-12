var PORT = 33333;
var HOST = '127.0.0.1';
const shell = require('shelljs');
var dgram = require('dgram');
var name_of_person = 'HarryJi'

var message = new Buffer(name_of_person);
//shell.exec('sh script.sh Pawan')

var server = require('ws').Server;
var s = new server({port: 5001});
//const shell = require('shelljs');
//var p= new server (port:5002)
var obj={lat:12.82082,lng:80.038229};
s.on('connection',function(ws){
	 ws.on('message',function(message){
	 	var mess = message.split(",");
	 	var name =mess[0];
	 	var emer_cont = mess[1];
	 	var license = mess[2];
	 	var lat = mess[3];
	 	var longi = mess[4];
	 	var acc = mess[5];
	 	var date = new Date();
	 	if(name=="John_Doe")
	 	{
	 	console.log("\n\n\n_____________________________________\n\nAccident occured at     : (" + lat+","+longi+")"+ 
	 														   "\nName                    : "+ name +
	 														   "\nEmergency Contact       :"+emer_cont+
	 														   "\nvehicle license plate   :"+license+
	 														   "\nNet acc                 :"+acc+
	 														   "\nDate and Time           :"+date+
	 														   "\n_____________________________________\n\n");
	 	}
	 	// const pdf = new jsPDF();
	 	// pdf.text(40,10,"Accident Report");
	 	// pdf.text(20,15,"This is to certify that " + name + " car having license no "+license+" met with an accident at"+date+" and Experienced max acceleration of "+acc+"ms-2." );
	  //   pdf.save();
         //var obj={lat:12.5656,lng:12.5656};
         //obj={lat:parseFloat(lat),lng:parseFloat(longi)};
         console.log(obj);
         const fs = require('fs');
         const PDFDocument = require('pdfkit');
         //console.log(lat);
// Create a document
		const doc = new PDFDocument;
	
// Pipe its output somewhere, like to a file or HTTP response
// See below for browser usage
		doc.pipe(fs.createWriteStream('Result1.pdf'));

// Embed a font, set the font size,"" and render some text
		//doc.font('fonts/PalatinoBold.ttf')
   		//	.fontSize(25)
		  doc.fontSize(25)
		  	 .text("\n       Proof of Accident\n\n",{align:'center'});
		  doc.fontSize(15)
		     .text("This is to certify that " + name + " car having license no "
		  	+license+" met with an accident at"+date+" and Experienced max acceleration of "
		  	+acc+"ms-2.");

		 doc.end();

	     var cmd="sh script.sh "+ emer_cont +" "+name+ " "+license+" "+lat+" "+longi+" "+date;
	// var obj = {lat:25.5941, lng:85.1376};
		s.clients.forEach(function e(client){
			if(client==ws)
			{
				client.send(message);
		        //shell.exec('sh script.sh Pawan');
		        //console.log(obj)
		        //ws.send(JSON.stringify(obj));
		        if(name=="John_Doe")
		        shell.exec(cmd);
			}
		});
		ws.on('close',function(){
			console.log("Client disconnected");
			
		});
		//ws.send(JSON.stringify(message));
	 });
});


/*
var client = dgram.createSocket('udp4');
client.send(message, 0, message.length, PORT, HOST, function(err, bytes) {
    if (err) throw err;
    //shell.exec('final.py')

    console.log('UDP message sent to ' + HOST +':'+ PORT);
    client.close();
});
*/