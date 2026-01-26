// { Driver Code Starts
import java.util.*;
class Sorting
{
	static void printArray(int arr[])
    {
        int n = arr.length;
        for (int i=0; i<n; ++i)
            System.out.print(arr[i]+" ");
        System.out.println();
    }
    
    // Driver program
    public static void main(String args[])
    {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		while(T>0)
		{
			int n = sc.nextInt();
			int arr[] = new int[n];
			for(int i=0;i<n;i++)
				arr[i] = sc.nextInt();

			
			new Solution().quickSort(arr,0,n-1);
			printArray(arr);
		    T--;
		}
} }// } Driver Code Ends


class Solution
{
     
    static int[] swap(int[] a,int e1,int e2)
    {
        int temp=a[e1];
        a[e1]=a[e2];
        a[e2]=temp;
        return a;
    }
    //Function to sort an array using quick sort algorithm.
    static void quickSort(int a[], int start, int end)
    {
        // code here
          if(start>=end)
        {
            return;
        }
        int i=partition(a,start,end);
        quickSort(a,start,i-1);
        quickSort(a,i+1,end);
    }
    static int partition(int a[], int start, int end)
    {
        // your code here
          int pindex=start;
        int pivot=a[pindex];
        int count=0;
        for(int i=start;i<=end;i++)
        {
            if(a[i]<pivot)
            {
                count++;
            }   
        }
        int nepindex=pindex+count;
        a=swap(a,pindex,nepindex);
        int i=start;
        int j=end;
        while(i<j)
        {
            if(a[i]<pivot)
            {
                i++;
              
            }
            if(a[j]>=pivot)
            {
                j--;
                 
            }
            if(i>=j)
            {
                break;
            }
            
            if(a[i]>pivot&&a[j]<pivot)
            {
                a=swap(a,i,j);
                i++;
                j--;
            }
            if(a[i]>a[j])
            {
                a=swap(a,i,j);
                
            }
           
            
        }
        return nepindex;
    } 
}