public class overflow{
	public static void main(String args[]){
		int importantData=1;
		int[] buffer = new int[10];

		for (int i=0;i<15;i++)
			buffer[i]=7;
		System.out.println("after a buffer overflow");
		System.out.println("Important data="+importantData);
	}
}
