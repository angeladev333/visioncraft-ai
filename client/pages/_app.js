import "../styles/globals.css";
import Navbar from "../components/Navbar";
import { Poppins } from "next/font/google";
import { NextUIProvider } from "@nextui-org/react";

const poppins = Poppins({
  subsets: ["latin-ext"],
  weight: ["300", "400", "600", "700"],
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
