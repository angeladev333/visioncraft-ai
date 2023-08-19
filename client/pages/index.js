import Head from "next/head";
import styles from "../styles/Home.module.css";
import { Hero } from "../components/Hero";
import { NextSeo } from "next-seo";
import Info from "../components/Info";

export default function Home() {
  return (
    <>
      <NextSeo
        title="VisionCraft"
        description="VisionCraft is a new way to capture and analyze your hardware setup,
        unlocking a wealth of possibilities"
        favicon="/favicon.ico"
      />
      <div>
        <Hero />
        <Info />
      </div>
    </>
  );
}
