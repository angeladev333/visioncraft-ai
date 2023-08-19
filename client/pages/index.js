import Head from "next/head";
import styles from "../styles/Home.module.css";

export default function Home() {
  return (
    <>
      <div className={styles.container}>
        <Head>
          <title>Our Amazing Company</title>
          <meta name="description" content="Our Amazing Company obviously" />
          <link rel="icon" href="/favicon.ico" />
        </Head>
        <h1 className={styles.title}>YOUR TOOLBOX, OUR CANVAS</h1>

        <style jsx>{`
          main {
            padding: 5rem 0;
            flex: 1;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
          }
        `}</style>
      </div>
    </>
  );
}
