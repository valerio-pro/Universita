package run.model;

public interface Data {
	
	int getYear();
	int getMonth();
	int getDay();
	void setYear(int year) throws YearException;
	void setMonth(int month) throws MonthException;
	void setDay(int day) throws DayException;
	void initialize(int day, int month, int year) throws DayException, MonthException, YearException;
	boolean isAnnoBisestile(int year);
	boolean equals(Data data);
	
}
