export interface Commune {
  id: string;
  type: string;
  slug: string;
  label: string;
  zip: number[];
  results: Results;
}

export interface Results {
  lastUpdateTime: string;
  percentageCounting: number;
  votePlace: VotePlace;
  parties: PartyResult[];
  voteTotalNew: number;
  voteTotalOld: number;
  seatTotalNew: number;
  seatTotalOld: number;
}

export interface VotePlace {
  done: number;
  total: number;
}

export interface PartyResult {
  id: string;
  name: string;
  slug: string;
  color: string;
  currentCount: number;
  previousCount: number;
  currentSeats: number;
  previousSeats: number;
}
