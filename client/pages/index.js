import Head from "next/head";
import styles from "../styles/Home.module.css";
import { Hero } from "../components/Hero";
import { NextSeo } from "next-seo";

export default function Home() {
  return (
    <>
      <NextSeo
        title="Our Amazing Company"
        description="Our Amazing Company obviously"
        favicon="/favicon.ico"
        />
      <div>
        <Hero />
      </div>
    </>
  );
}
