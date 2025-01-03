# AccessVerifier

W firmie ACME istnieje mikroserwis ClientDataManager w klastrze K8s Azure. Dostęp do niego ze świata odbywa się poprzez publiczny ingress. Klientem mikroserwisu jest w 100% aplikacja działająca w AWS w regionie Europe West.
Podczas spotkania nt. bezpieczeństwa zdecydowaliście w zespole, że dostęp do tego mikroserwisu zostanie dodatkowo zabezpieczony przez ograniczenie puli dozwolonych adresów IP do adresów AWS z odpowiedniego regionu.
W tym celu przygotujecie mikroserwis AccessVerifier:

    za każdym razem otrzymując request HTTP, ClientDataManager wyśle do AccessVerifier pełny, niezmodyfikowany nagłówek HTTP otrzymanego requestu jako text/plain,
    AccessVerifier zwróci odpowiedź 200 OK lub 401 Unauthorized – w zależności od tego, czy ruch ma zostać dopuszczony czy nie,
    AccessVerifier raz na dobę będzie odświeżał sobie dane adresacji, które ma dopuścić.

Wybraną przez Was technologią jest Python.