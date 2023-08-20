import "../styles/globals.css";
import Navbar from "../components/Navbar";
import { Poppins } from "next/font/google";
import AOSLoader from "../components/AOSLoader";
import "aos/dist/aos.css";
import { useEffect } from "react";
import { useRouter } from "next/router";
import Head from "next/head";

const poppins = Poppins({
  subsets: ["latin-ext"],
  weight: ["300", "400", "600", "700"],
  display: "swap",
});

export default function App({ Component, pageProps }) {
  const router = useRouter();

  useEffect(() => {
    const handleRouteChange = () => {
      if (window.AOS) {
        window.AOS.refresh();
      }
    };

    router.events.on("routeChangeComplete", handleRouteChange);

    return () => {
      router.events.off("routeChangeComplete", handleRouteChange);
    };
  }, []);

  return (
    <>
      <Head>
        <link
          href="https://unpkg.com/aos@2.3.1/dist/aos.css"
          rel="stylesheet"
        />
        <script src="https://unpkg.com/aos@2.3.1/dist/aos.js" async></script>
      </Head>

      <AOSLoader />
      <main className={`${poppins.className}`}>
        <Navbar />
        <Component {...pageProps} />
      </main>
    </>
  );
}
