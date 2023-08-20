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
    <div className="flex flex-col items-center justify-center min-h-screen mb-12 bg-fixed bg-center bg-cover custom-img">
      <div className="text-center z-10">
      <div className="bg-white p-4 rounded shadow-md rounded-3xl pb-20">
        <h2 className="text-4xl font-bold p-6 text-violet-500">BUILD</h2>

        <h1 className="text-5xl w-2/3 break-normal mx-auto mb-10 p-6 font-extrabold">
          Upload any image and we'll find what you can create
        </h1>
      
      
      <div className="px-60 gap-10 grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3">
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



        <div className="flex-1">
            <Image
              width={300} 
              height={300} 
              alt="Imagination"
              className="w-full h-full object-cover pl-10" 
              src="/imagination.jpg"
            />
          </div>


        <div className="flex-1">
           
            <p className="text-3xl text-gray-900 dark:text-white">
              Use your desires to craft personalized creations with step-by-step guidance
            </p>
          </div>
        




        </div>




      

      </div>

     

    </div>
  );
}

