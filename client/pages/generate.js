import React from "react";
import ImageForm from "../components/ImageForm";
import { NextSeo } from "next-seo";

export default function Generate() {
  return (
    <>
      <NextSeo
        title="Generate | VisionCraft"
        description="VisionCraft is a new way to capture and analyze your hardware setup,
        unlocking a wealth of possibilities"
      />

      <main className="bg-[url('/Group_35512.png')] bg-cover bg-bottom">
        <div className="flex items-center justify-center h-screen ">
          <div className="bg-white rounded w-full m-2 md:m-20 h-[100vh-50px]">
            <ImageForm />
          </div>
        </div>
        {/* <img className="z-50 w-full absolute overflow-hidden" src="/Group_35512.png" /> */}
      </main>
    </>
  );
}
