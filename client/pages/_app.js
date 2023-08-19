import "../styles/globals.css";
import Navbar from "../components/Navbar";
import { Poppins } from "next/font/google";

const poppins = Poppins({
  subsets: ["latin-ext"],
  weight: ["300", "600"],
  display: "swap",
});

export default function App({ Component, pageProps }) {
  return (
    <>
      <main className={`${poppins.className}`}>
        <Navbar />
        <Component {...pageProps} />
      </main>
    </>
  );
}
