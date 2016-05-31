package org.cesitech.lucie.nico.fr.service;

import java.io.DataOutputStream;
import java.io.InputStreamReader;
import java.net.Socket;
import java.rmi.server.UID;

import org.cesitech.lucie.nico.fr.LaunchServer;

public class Service extends Thread{
	private Socket socketService;
	private LaunchServer launchServer;
	
	private InputStreamReader in;
	private DataOutputStream out;
	
	private UID ID;
	
	private boolean isRunning = false;
	
	public Service(Socket accept, LaunchServer launchServer) {
		this.socketService = accept;
		ID = new UID();
		this.launchServer = launchServer;
	}

	@Override
	public void run() {
		try{
			out = new DataOutputStream(socketService.getOutputStream());
			in = new InputStreamReader(socketService.getInputStream());
		}catch(Exception ex){
			ex.printStackTrace();
		}
		isRunning = true;
		//send("Test de vérification");
		String code = "";
		boolean message = false;
		long milliseconde = 0;
		do{
			try{
				int idChar = -1;
				while(idChar < 0 && isRunning){
					idChar = in.read();
					code += (char)idChar;
					if(idChar >= 0){
						if(!message)milliseconde = System.nanoTime();
						message = true;
					}
					if(code.contains(";")){
						packet(code, milliseconde);
						message = false;
						code = "";
					}
				}
			}catch(Exception ex){
				ex.printStackTrace();
				isRunning = false;
			}
		}while(isRunning );
	}

	public void packet(String code, long milliseconde) {
		code = code.replace(";", "");
		System.out.println(code);
		System.out.println("Temps de réponse : "+(System.nanoTime()-milliseconde)/1000000.0+" ms");
		if(code.equals("getCoord()")){
			System.out.println("=>t");
			send("Bonjour");
			System.out.println("=>t");
		}
	}

	public void sendOther(String object){
		launchServer.sendAllOther(object, ID);
	}
	public void send(String object) {
		try{
			out.writeBytes(object);
			out.flush();
		}catch(Exception ex){
			isRunning = false;
			ex.printStackTrace();
		}
	}
	
	public UID getID(){
		return ID;
	}
	
	public boolean isRunning(){
		return isRunning;
	}
}
