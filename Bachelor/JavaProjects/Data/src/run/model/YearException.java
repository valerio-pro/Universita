package run.model;

@SuppressWarnings("serial")
public class YearException extends Exception {
	
	public YearException(int year) {
		super("L'anno scelto " + year + " non e' consentito");
	}
	
}
