import { PythonShell } from 'python-shell'
import { spawn } from 'child_process'
// let grabber = spawn('python3', {argv0: 'grab.py 18 30'})
let grabber = new PythonShell('grab.py', { args: ['18', '30'] })

let counter = 0

grabber.stdout.on('data', () => {
    console.timeEnd(counter + '')
})

setInterval(() => {
    console.log('sending attempt ' + counter++)
    grabber.send('')
    console.time(counter + '')
}, 2000)