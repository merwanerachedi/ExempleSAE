import java.rmi.*;
    import java.rmi.server.*;


public class CalculatriceImpl extends UnicastRemoteObject implements Calculatrice {

    public CalculatriceImpl() throws RemoteException {
        super();
    }

    public double additionner(double a, double b) throws RemoteException {
        return a + b;
    }

    public double multiplier(double a, double b) throws RemoteException {
        return a * b;
    }
}
