import java.rmi.*;

// Interface accessible à distance par le client.
public interface Calculatrice extends Remote {
    // Les méthodes distantes doivent déclarer RemoteException.
    double additionner(double a, double b) throws RemoteException;

    double multiplier(double a, double b) throws RemoteException;
}
