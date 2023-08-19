import Head from "next/head";
import styles from "../styles/Home.module.css";
import { Hero } from "../components/Hero";

export default function Home() {
  return (
    <>
      <div>
        <Head>
          <title>Our Amazing Company</title>
          <meta name="description" content="Our Amazing Company obviously" />
          <link rel="icon" href="/favicon.ico" />
        </Head>
        <Hero />
      </div>
    </>
  );
}
