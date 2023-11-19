


public class WebServer
{
    public static void main(String[] args)
    {
      try(ServerSocket serverSocket = new ServerSocket(8088))
      {
        Socket = serverSocket.accept();
        System.out.println("New client connected!");
      }
      
      catch (IOException e)
      {
        
        e.printStackTrace();
      }  
    }
}