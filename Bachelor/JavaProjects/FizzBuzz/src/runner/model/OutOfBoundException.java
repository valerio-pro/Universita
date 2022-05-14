package runner.model;

@SuppressWarnings("serial")
public class OutOfBoundException extends Exception {
	
	public OutOfBoundException(int n) {
		
		super("Il numero inserito " + n + " non e' accettabile");
	
	}
	
}
