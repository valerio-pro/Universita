package run.model;

@SuppressWarnings("serial")
public class MonthException extends Exception {
	
	public MonthException(int month) {
		super("Il mese scelto " + month + " non e' consentito");
	}
	
}
