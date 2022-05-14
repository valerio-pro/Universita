package Runners;

import java.io.*;
import java.net.*;

public class Server_Runner {

	public static void main(String[] args) throws IOException {
		
		String request = " ", answer;
		int gate = 1234;
		
		ServerSocket socketAscolto = new ServerSocket(gate);
		System.out.println("Server in ascolto sulla porta " + gate);
		
		Socket connectionSocket = socketAscolto.accept();   // process waits for connection request
		BufferedReader in_client = new BufferedReader(new InputStreamReader(connectionSocket.getInputStream()));
		DataOutputStream out = new DataOutputStream(connectionSocket.getOutputStream());
		
		while(!request.equalsIgnoreCase("exit")) {
			
			request = in_client.readLine();
			answer = request.toUpperCase() + "\n";
			out.writeBytes(answer);
			
		}
		
		connectionSocket.close();
		socketAscolto.close();
		
	}

}
