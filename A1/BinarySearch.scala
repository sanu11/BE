object BinarySearch
{
	def main(args : Array[String])
	{
		println("Enter number of elements")
		var n = Console.readInt()

		println("Enter elements")	

		var arr=new Array[Int](n)

		for(i<-0 to n-1)
			arr(i)=Console.readInt

		scala.util.Sorting.quickSort(arr)

		println("Sorted elements")
		for(i<-0 to n-1)
			println(arr(i))


		println("Enter element to search")
		var key=Console.readInt()

		var res=BinarySearch(arr,key,0,n-1)
		println("Element found at position " + res);
	}


	def BinarySearch(arr:Array[Int],key:Int, start:Int,end:Int) :Int = {

	if(start>end)
	return -1

	var mid=(start+end)/2

	if(arr(mid)==key)
		return mid;

	else if (key < arr(mid))
		return BinarySearch(arr,key,start,mid);

	else 
		return BinarySearch(arr,key,mid+1,end);

	}

}
