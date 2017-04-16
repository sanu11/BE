import java.util.ArrayList;
import java.util.Calendar;
import java.util.LinkedList;
import java.util.List;
import org.cloudbus.cloudsim.*;
import org.cloudbus.cloudsim.core.CloudSim;
import org.cloudbus.cloudsim.provisioners.BwProvisionerSimple;
import org.cloudbus.cloudsim.provisioners.PeProvisionerSimple;
import org.cloudbus.cloudsim.provisioners.RamProvisionerSimple;

public class Cloud
{
	private static List<Vm>vmList;
	private static List<Cloudlet>cloudletList;
	public static void main(String args[]){
		int num_users = 1;
		Calendar calender = Calendar.getInstance();
		int traceFlag=0;
		//1
		CloudSim.init(num_users, calender,false);
		//2
		try {
			Datacenter datacenter = createDatacenter("Datacenter0");
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		//3
		DatacenterBroker datacenterbroker = createBroker();
		int broker_id = datacenterbroker.getId();
		//4
		vmList = new ArrayList<Vm>();
		int vmid = 0;
		int userId = broker_id;
		int mips=1000;
		int numberOfPes = 1; //cpus
		int ram = 512;
		int bw=1000;
		int size=10000;
		String vmm="Xen";
		
		Vm vm = new Vm(vmid, userId, mips, numberOfPes, ram, bw, size, vmm, new CloudletSchedulerTimeShared());
		vmList.add(vm);
		datacenterbroker.submitVmList(vmList);
		
		//5
		cloudletList = new ArrayList<Cloudlet>();
		int cloudletId =0;
		long cloudletLength = 400000;
		long cloudletFileSize =300;
		int pesNumber = 1;
		long cloudletOutputSize = 300;
		UtilizationModel utilizationModel = new UtilizationModelFull();
		
		Cloudlet cloudlet = new Cloudlet(cloudletId, cloudletLength, pesNumber, cloudletFileSize, cloudletOutputSize, utilizationModel, utilizationModel,utilizationModel, false);
		cloudlet.setUserId(broker_id);
		cloudlet.setVmId(vmid);
		
		cloudletList.add(cloudlet);
		datacenterbroker.submitCloudletList(cloudletList);
		CloudSim.startSimulation();
		CloudSim.stopSimulation();
		
		List<Cloudlet>newlist = datacenterbroker.getCloudletReceivedList();
		printCloudletObjects(newlist);
	}
	private static void printCloudletObjects(List<Cloudlet> newlist) {
		int size = newlist.size();
		String indent = "         ";
		String indent2= "     ";
		Cloudlet cloudlet;
		System.out.println("CloudLet Id  " + indent2 + "STATUS " + indent2 + "DATACENTER ID " + indent2 + " VM ID "
		+ indent2 +"TIME " + indent2 + "START TIME " + indent2 + "END TIME " );
		
		for (int i=0;i<size;i++){
			cloudlet = newlist.get(i);
			String status = "";
			if(cloudlet.getStatus() == Cloudlet.SUCCESS)
				status ="SUCCESS";
			System.out.println(cloudlet.getCloudletId() + indent +"   "+cloudlet.getCloudletStatus()+ " " + status+ indent+
					cloudlet.getAllResourceId()+ indent  + "   "+ cloudlet.getVmId() + indent + cloudlet.getActualCPUTime()
					+ indent + cloudlet.getExecStartTime() + indent + cloudlet.getFinishTime());
			
		}
		// TODO Auto-generated method stub
		
	}
	private static DatacenterBroker createBroker() {
		DatacenterBroker datacenterBroker = null;
		try {
			datacenterBroker = new DatacenterBroker("broker0");
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return datacenterBroker;
		
	// TODO Auto-generated method stub
		
		
	}
	private static Datacenter createDatacenter(String name) throws Exception {
		// TODO Auto-generated method stub
		String architecture = "x86";
		String os = "Linux";
		String vmm = "Xen";
		double costPerBw = 0.0;
		double costPerMem = 0.05 ;
		double costPerSec = 3.0;
		double costPerStorage = 0.01;
		double timeZone = 10.0;
		
		List<Host>hostList = new ArrayList<Host>();
		List<Pe>peList = new ArrayList<Pe>();
		peList.add(new Pe(0, new PeProvisionerSimple(1000)));
		int id=0;
		int bw = 10000;
		int ram=2048;
		long storage = 1000000;
	
		hostList.add( new Host(id, new RamProvisionerSimple(ram), new BwProvisionerSimple(bw), storage, peList, new VmSchedulerTimeShared(peList)));
		DatacenterCharacteristics characteristics = new DatacenterCharacteristics(architecture, os, vmm, hostList, timeZone, costPerSec, costPerMem, costPerStorage, costPerBw); 
		LinkedList<Storage> storageList = new LinkedList<Storage>();
		Datacenter datacenter = null;
		datacenter =  new Datacenter(name, characteristics, new VmAllocationPolicySimple(hostList), storageList, 0);
		return datacenter;
		
	}
}