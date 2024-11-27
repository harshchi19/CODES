import java.net.*;
import java.util.Scanner;

public class UDP_Client {
    public static void main(String[] args) {
        try (DatagramSocket socket = new DatagramSocket(); Scanner scanner = new Scanner(System.in)) {
            InetAddress server = InetAddress.getByName("localhost");
            int port = 9876;

            System.out.println("Type messages to send:");
            while (true) {
                // Send message
                byte[] sendData = scanner.nextLine().getBytes();
                socket.send(new DatagramPacket(sendData, sendData.length, server, port));

                // Receive response
                byte[] receiveData = new byte[1024];
                DatagramPacket response = new DatagramPacket(receiveData, receiveData.length);
                socket.receive(response);

                System.out.println("Server: " + new String(response.getData(), 0, response.getLength()));
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
