package org.cesitech.lucie.nico.fr;

import java.net.ServerSocket;
import java.rmi.server.UID;
import java.util.ArrayList;

import org.cesitech.lucie.nico.fr.service.Service;

public class LaunchServer {
	private ServerSocket serverSocket;
	
	private int port;
	private boolean isRunning = false;
	
	public static int MAX_SERVICES = 10;
	
	public ArrayList<Service> services;
	
	public LaunchServer(int port){
		this(port, MAX_SERVICES);
	}
	public LaunchServer(int port, int limiteNbr) {
		MAX_SERVICES = limiteNbr;
		this.port = port;
		startServer();
		
		try{
			serverSocket = new ServerSocket(this.port, MAX_SERVICES);
			services = new ArrayList<Service>();
			System.out.println("Ouverture du serveur au port : "+this.port);
			System.out.println("Serveur on !");
			while(isRunning()){
				Service s = new Service(serverSocket.accept(), this);
				services.add(s);
				services.get(services.indexOf(s)).start();
			}
		}catch(Exception ex){
			ex.printStackTrace();
		}finally{
			closeServer();
		}
	}
	public void sendAll(String object){
		for(Service s : services){
			if(s.isRunning())
				s.send(object);
		}
	}
	public void sendAllOther(String object, UID id){
		for(Service s : services){
			if(s.isRunning())
				if(s.getID() != id)
					s.send(object);
		}
	}
	public void closeServer() {
		
	}
	public void startServer() {
		setRunning(true);
	}
	
	public void setRunning(boolean isRunning){
		this.isRunning = isRunning;
	}
	
	public boolean isRunning() {
		return isRunning;
	}
	
	public static void main(String[] args){
		new LaunchServer(6009, 20);
	}
}
