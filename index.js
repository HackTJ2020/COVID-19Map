const spawn = require('child_process').spawn;
setInterval(function A() { 
    const process = spawn('python', ['./mainTSF.py']);
}, 43200000); 
// process.stdout.on('data', data => {
//     console.log(data.toString());
// });