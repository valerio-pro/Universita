package run;

import run.model.Data;
import run.model.DayException;
import run.model.MonthException;
import run.model.YearException;
import run.model.impl.DataObject;

public class Runner {

	public static void main(String[] args) throws DayException, MonthException, YearException {
		
		Data data1 = new DataObject(29,2,2000);
		Data data2 = new DataObject(13,12,2000);
		
		Data data3 = new DataObject(2,2,1980);
		Data data4 = new DataObject(2,10,1990);
		Data data5 = new DataObject(12,2,1978);
		
		System.out.println(data1);
		System.out.println("\n" + data2);
		System.out.println("\n" + data3);
		System.out.println("\n" + data4);
		System.out.println("\n" + data5);
		
		System.out.println("\n" + data1.equals(data2));
		System.out.println("\n" + data1.equals(data3));
		
	}

}
