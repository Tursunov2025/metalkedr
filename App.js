import { useState } from "react";
import axios from "axios";

function App() {

  const [telefon, setTelefon] = useState("");
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [parol, setParol] = useState("");

  const login = () => {

    axios.post("http://127.0.0.1:5000/login", {
      telefon: telefon,
      parol: parol
    })
      .then((response) => {

        setIsLoggedIn(true);

      })
      .catch(() => {

        alert("Login yoki parol xato");

      });

  };

  if (isLoggedIn) {

  return (

    <div style={{
      background: "#111",
      minHeight: "100vh",
      color: "white",
      padding: 20
    }}>

      <h1 style={{
        color: "gold"
      }}>
        MetalKedir Dashboard
      </h1>

      <h2>
        Tizimga muvaffaqiyatli kirildi 😎
      </h2>

    </div>

  );

}
  return (
    <div style={{
      background: "#111",
      minHeight: "100vh",
      display: "flex",
      justifyContent: "center",
      alignItems: "center"
    }}>

      <div style={{
        background: "#1e1e1e",
        padding: 40,
        borderRadius: 20,
        width: 350,
        boxShadow: "0 0 20px rgba(255,215,0,0.3)"
      }}>

        <h1 style={{
          color: "gold",
          textAlign: "center",
          marginBottom: 30
        }}>
          MetalKedir
        </h1>

        <input
          placeholder="Telefon"
          value={telefon}
          onChange={(e) => setTelefon(e.target.value)}
          style={{
            width: "100%",
            padding: 15,
            marginBottom: 15,
            borderRadius: 10,
            border: "none",
            fontSize: 16
          }}
        />

        <input
          type="password"
          placeholder="Parol"
          value={parol}
          onChange={(e) => setParol(e.target.value)}
          style={{
            width: "100%",
            padding: 15,
            marginBottom: 20,
            borderRadius: 10,
            border: "none",
            fontSize: 16
          }}
        />

        <button
          onClick={login}
          style={{
            width: "100%",
            padding: 15,
            background: "gold",
            border: "none",
            borderRadius: 10,
            fontWeight: "bold",
            cursor: "pointer",
            fontSize: 16
          }}
        >
          Kirish
        </button>

      </div>

    </div>
  );
}

export default App;