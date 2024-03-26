import React from 'react';
import Layout from '../../components/Layout/Layout';
import CtaButton from '../../components/misc/CtaButton';
import SeoHead from '../../components/SeoHead';
import YouTubeEmbed from '../../components/misc/YouTubeEmbed';

const StartUpsNewsletter = () => {
  return (
    <>
      <SeoHead title="Start-Ups Newsletter" />
      <Layout>
        <div className="container mx-auto px-4 py-8 mt-16">
            <CtaButton text="Free forever for 2 podcasts!" href="https://github.com/luke-harriman/podcast-summariser" />
          <h1 className="text-3xl font-bold text-center my-4">
            Start Ups Newsletter: This Week In Start Ups, All-In Podcast & The Tim Feris Show.
          </h1>
          <div className="flex justify-around gap-4">
            <YouTubeEmbed videoId="6NR7ntVo8F8" />
            <YouTubeEmbed videoId="3tEcLAud7Nc" />
            <YouTubeEmbed videoId="_htIvi4JzOs" />
          </div>
          <div className="max-w-3xl mx-auto text-center">
            <h2 className="text-2xl font-bold mt-8">
              This Week In Start-Ups: Kleiner Perkins and Penn’s Endowment on India, loss ratios, and the rise of secondaries | E1919
            </h2>
            <p>
              Video summaries or text content goes here...
            </p>
          </div>
        </div>
      </Layout>
    </>
  );
};

export default StartUpsNewsletter;