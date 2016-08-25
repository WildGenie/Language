use std::io::Read;
use std::io::Write;
use std::net::{TcpListener, TcpStream};
use std::thread;

fn handle_client(mut stream: TcpStream) {
    let mut buf = [0u8, 255];
    loop {
        let buf_read = stream.read(&mut buf).unwrap();
        if buf_read == 0 {
            break;
        }
        println!("{:?}", buf);
        stream.write_all(&buf).unwrap();
    }
}

fn main() {
    let listener = TcpListener::bind("127.0.0.1:80").unwrap();
    for stream in listener.incoming() {
        match stream {
            Err(log) => println!("{:?}", log),
            Ok(mut stream) => {
                stream.write_all(b"Connected\n\n").unwrap();
                thread::spawn(move || {
                    handle_client(stream);
                });
            },
        };
    }

    drop(listener);
}