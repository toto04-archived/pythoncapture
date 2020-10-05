import { Grabber } from './grabber'
import { createSocket } from 'dgram'

let client = createSocket('udp4')
let grabber = new Grabber(10, 18)

setInterval(async () => {
    let buf = await grabber.grab()
    client.send(buf, 4210, '192.168.1.22')
}, 200)