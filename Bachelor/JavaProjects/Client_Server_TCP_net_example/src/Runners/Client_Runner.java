package Runners;

import java.io.*;
import java.net.*;

public class Client_Runner {

	public static void main(String[] args) throws UnknownHostException, IOException {
		
		String serverName = "localhost";
		int gate = 1234;
		String request = " ";
		String answer;
		
		BufferedReader in_keyboard = new BufferedReader(new InputStreamReader(System.in));
		Socket clientSocket = new Socket(serverName, gate);		
		DataOutputStream out = new DataOutputStream(clientSocket.getOutputStream());
		BufferedReader in_server = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
		
		while(!request.equalsIgnoreCase("exit")) {
			
			System.out.print("Write a sentence: ");
			request = in_keyboard.readLine(); // bloccante
			out.writeBytes(request + "\n");
			answer = in_server.readLine(); // bloccante
			System.out.println("Answer from server: " + answer);
			
		}
		
		clientSocket.close();
		
	}

}
