import { useEffect } from "react";
import { useRouter } from "next/router";

const AOSLoader = () => {
  const router = useRouter();

  const initAOS = () => {
    if (window.AOS) {
      window.AOS.refresh();
      window.AOS.init({
        once: false,
      });
    }
  };

  useEffect(() => {
    // This will initialize AOS on component mount (initial load)
    initAOS();

    const handleRouteChange = () => {
      initAOS();
    };

    router.events.on("routeChangeComplete", handleRouteChange);

    return () => {
      router.events.off("routeChangeComplete", handleRouteChange);
    };
  }, []);

  return null;
};

export default AOSLoader;
