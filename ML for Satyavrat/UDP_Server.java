import java.net.*;

public class UDP_Server {
    public static void main(String[] args) {
        try (DatagramSocket socket = new DatagramSocket(9876)) {
            System.out.println("Server is running...");
            byte[] buffer = new byte[1024];

            while (true) {
                // Receive message
                DatagramPacket packet = new DatagramPacket(buffer, buffer.length);
                socket.receive(packet);
                String message = new String(packet.getData(), 0, packet.getLength());
                System.out.println("Received: " + message);

                // Send response
                String response = "Server received: " + message;
                byte[] responseData = response.getBytes();
                socket.send(new DatagramPacket(responseData, responseData.length, packet.getAddress(), packet.getPort()));
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
