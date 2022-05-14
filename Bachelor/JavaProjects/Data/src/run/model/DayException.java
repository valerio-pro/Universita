package run.model;

@SuppressWarnings("serial")
public class DayException extends Exception {
	
	public DayException(int day) {
		super("Il giorno scelto " + day + " non e' consentito");
	}

}
