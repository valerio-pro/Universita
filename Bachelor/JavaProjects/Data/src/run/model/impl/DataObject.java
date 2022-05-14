package run.model.impl;

import java.time.YearMonth;

import run.model.Data;
import run.model.DayException;
import run.model.MonthException;
import run.model.YearException;

/* gg/mm/aaaa format */

public class DataObject implements Data {
	
	private int day, month, year;
	
	public DataObject(int day, int month, int year) throws DayException, MonthException, YearException {
		
		try {
			initialize(day, month, year);
		} catch (DayException e) {
			e.printStackTrace();
		} catch (MonthException e) {
			e.printStackTrace();
		} catch (YearException e) {
			e.printStackTrace();
		}
		
	}
	
	public String toString() {
		
		if (month >= 1 && month <= 9 && day >= 10) return day + "/0" + month + "/" + year;
		else if (month >= 1 && month <= 9 && day <= 9) return "0" + day + "/0" + month + "/" + year;
		else if (month >= 10 && day <= 9) return "0" + day + "/" + month + "/" + year;
		else return day + "/" + month + "/" + year;  // month >= 10 && day >= 10
		
	}
	
	
	// L'ordine con cui vengono inizializzati conta... Il giorno DEVE essere inizializzato per ultimo 
	private void initialize(int day, int month, int year) throws DayException, MonthException, YearException {

		setYear(year);
		setMonth(month);
		setDay(day);
		
	}
	
	public boolean isAnnoBisestile(int year) {
		
		if ( ((year%4 == 0) && (year%100 != 0)) || (year%400 == 0) ) return true;
		return false;
		
	}
	
	public boolean equals(Data data) {
		
		if ( (this.getDay() == data.getDay()) && (this.getMonth() == data.getMonth()) && (this.getYear() == data.getYear()) ) return true;
		return false;
		
	}
	
	
	// GETTERS
	
	public int getDay() {
		return day;
	}

	public int getMonth() {
		return month;
	}
	
	public int getYear() {
		return year;
	}

	
	// PRIVATE SETTERS

	private void setYear(int year) throws YearException {
		
		int currentYear = YearMonth.now().getYear();
		
		if (year > 1900 && year <= currentYear) this.year = year;
		else throw new YearException(year);
		
	}
	
	private void setMonth(int month) throws MonthException {
		
		if (month <= 12 && month >= 1) this.month = month;
		else throw new MonthException(month);
		
	}
	
	private void setDay(int day) throws DayException {
		
		if (month == 1 || month == 3 || month == 5 || month == 7 || month == 8 || month == 10 || month == 12) {
			
			if (day >= 1 && day <= 31) this.day = day;
			else throw new DayException(day);
			
		}
		
		else if(month == 4 || month == 6 || month == 9 || month == 11) {
			
			if (day >= 1 && day <= 30) this.day = day;
			else throw new DayException(day);
			
		}
			
		else {
			
			if (this.isAnnoBisestile(year)) {
				
				if (day >= 1 && day <= 29) this.day = day;
				else throw new DayException(day);
				
			}
			
			else {
				
				if (day >= 1 && day <= 28) this.day = day;
				else throw new DayException(day);
				
			}
			
		}
		
	}
	
	
}
