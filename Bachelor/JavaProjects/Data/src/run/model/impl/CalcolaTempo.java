package run.model.impl;

import java.sql.Time;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Random;

public final class CalcolaTempo {

	
	public static long getSecondiInIntervalloTemporale(String oraIniziale, String oraFinale) throws ParseException {
		
		SimpleDateFormat format = new SimpleDateFormat("HH:mm:ss");   // formato ore:minuti:secondi, per esempio "18:30:26"
		
		Date data1, data2;
		
		long differenza = 0;
		
		data1 = format.parse(oraIniziale);
		data2 = format.parse(oraFinale);
		
		differenza = data2.getTime() - data1.getTime();         // differenza e' misurata in millisecondi
		
		return differenza/1000;  // ritorna in secondi
		
	}
	
	
	public static String getRandomHour() {
		
		final Random random = new Random();
		final int millisInDay = 24*60*60*1000;
		Time time = new Time((long)random.nextInt(millisInDay));
		
		return String.valueOf(time);
		
	}
	
	
}
