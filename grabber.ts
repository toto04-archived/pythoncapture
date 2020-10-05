import { PythonShell } from 'python-shell'

export class Grabber {
    script: PythonShell
    constructor(height: number, width: number) {
        this.script = new PythonShell('grab.py', {
            pythonPath: 'C:\\Users\\toto0\\AppData\\Local\\Programs\\Python\\Python38-32\\python.exe',
            args: [height + '', width + '']
        })
    }

    grab = () => new Promise<Buffer>(res => {
        this.script.once('message', (message: string) => {
            let arr: string[] = [];
            let pixels = message.split(',')
            pixels.forEach(pixel => arr.push(...pixel.match(/.{1,2}/g)))
            res(Buffer.from(arr.map(hex => parseInt(hex, 16))))
        })
        this.script.send('')
    })
}