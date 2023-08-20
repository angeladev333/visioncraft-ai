import React from "react";
import { Card, CardHeader, CardBody, CardFooter } from "@nextui-org/react";
import Image from "next/image";

export default function Info() {
  const list = [
    {
      img: "/image1.png",
    },
    {
      img: "/image2.png",
    },
    {
      img: "/image3.png",
    },
  ];



  return (
    <>
    
    <div className="bg-slate-100 pt-36 pb-16" >

    <div className="mt-8 bg-slate-100 p-4 rounded-3xl pb-40">
    <h2 className="text-8xl font-bold pr-40 px-40 bg-clip-text text-transparent bg-gradient-to-t from-violet-500 to-blue-400 text-center ">
    Explore, catalog, and optimize your hardware components.
        </h2>

        </div>

    <div className="flex flex-col items-center justify-center min-h-screen bg-fixed bg-center bg-cover custom-img">
      <div className="text-center z-10" id="features">
        <div className="bg-white p-4 rounded shadow-md rounded-3xl pb-20">
          <h2 className="text-4xl font-bold p-6 text-violet-500">BUILD</h2>

          <h1 className="text-5xl w-2/3 break-normal text-black mx-auto mb-10 p-6 font-extrabold">
            Upload any image and we'll find what you can create
          </h1>


          <div className="max-w-4xl px-2 mx-auto gap-10 grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3">
            {list.map((item, index) => (
              <Card
                shadow="sm"
                key={index}
                isPressable
                onPress={() => console.log("item pressed")}
                className="p-0"


              >
                <CardBody className="p-0">
                  {" "}
                  <Image
                    width={2400}
                    height={2400}
                    alt={item.title}
                    className="w-full h-full object-cover"
                    src={item.img}

                  />
                </CardBody>
                {/* CardFooter content */}
              </Card>
            ))}


          </div>
        </div>




        <div className="mt-8 bg-white p-4 rounded shadow-md rounded-3xl pb-20">
          <h2 className="text-4xl font-bold p-6 text-violet-500">TRANSFORM</h2>

          <h1 className="text-5xl w-2/3 break-normal mx-auto mb-10 p-6 font-extrabold">
            Turn Your Visions into Reality
          </h1>


          <div className="px-2 max-w-4xl mx-auto sm:flex h-96">
            <div className="w-full sm:w-1/2">
              <Image
                width={300}
                height={300}
                alt="Imagination"
                className="w-full h-full object-cover rounded-3xl"
                src="/imagination.jpg"
              />
            </div>


            <div className="flex w-full sm:w-1/2 items-center justify-center">

              <p className="px-2 sm:px-12 text-3xl text-gray-900">
                Use your desires, budget, and materials to craft personalized creations with step-by-step guidance
              </p>
            </div>
            
          </div>

        </div>
        <Card className="bottom-0 left-0 right-0 bg-black text-white mt-7">
        <footer class="bottom-0 left-0 right-0 bg-black rounded-3xl shadow m-4">
          <div class="w-full mx-auto max-w-screen-xl p-4 md:flex md:items-center md:justify-between">
            <span class="text-sm text-gray-500 sm:text-center dark:text-gray-400">© 2023 VisionCraft.ai™. All Rights Reserved.
          </span>
        
          </div>
      </footer>
      </Card>
      </div>
      
    </div>
    
    </div>
    </>
  );
}

