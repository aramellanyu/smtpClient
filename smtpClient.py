from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    # Fill in start
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((port, mailserver))
    # Fill in end

    recv = clientSocket.recv(1024).decode()
    #print(recv) #You can use these print statement to validate return codes from the server.
    #if recv[:3] != '220':
    #    print('220 reply not received from server.')

    # Send HELO command and print server response.
    helloCommand = 'HELLO Alice\r\n'
    clientSocket.send(helloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print(recv1)
    if recv1[:3] != '250':
        print('250 reply not received from server.')

    # Send MAIL FROM command and handle server response.
    # Fill in start
    mailFrom = 'MAIL FROM: <alyssanramella@gmail.com>\r\n'
    clientSocket.send(mailFrom.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print(recv1)
    if recv1[:3] != '250':
        print('250 reply not received from server.')
    # Fill in end

    # Send RCPT TO command and handle server response.
    # Fill in start
    rcptTo = 'RCPT TO: <anr9962@nyu.edu> \r\n'
    clientSocket.send(rcptTo.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print("After RCPT TO command: " + recv1)
    if recv1[:3] != '250':
        print('250 reply not received from server.')
    # Fill in end

    # Send DATA command and handle server response.
    # Fill in start
    data = 'DATA\r\n'
    clientSocket.send(data.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print("After DATA command: " + recv1)
    if recv1[:3] != '250':
        print('250 reply not received from server.')
    # Fill in end

    # Send message data.
    # Fill in start
    subject = "Subject: SMTP mail client testing \r\n\r\n"
    clientSocket.send(subject.encode())
    message = ("Enter your message: \r\n")
    clientSocket.send(message.encode())
    clientSocket.send(endmsg.encode())
    recv_msg = clientSocket.recv(1024)
    #print("Response after sending message body:" + recv_msg.decode())
    if recv1[:3] != '250':
        print('250 reply not received from server.')
    # Fill in end

    # Message ends with a single period, send message end and handle server response.
    # Fill in start
    clientSocket.send('.\r\n')
    recv1 = clientSocket.recv(1024)
    #print(recv1)
    if recv1[:3] != '250':
        print('250 reply not received from server.')
    # Fill in end

    # Send QUIT command and handle server response.
    # Fill in start
    quit = 'QUIT\r\n'
    clientSocket.send(quit.encode())
    recv1 = clientSocket.recv(1024)
    # print(message)
    if recv1[:3] != '250':
        print('250 reply not received from server.')
    #clientSocket.close()
    # Fill in end


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
