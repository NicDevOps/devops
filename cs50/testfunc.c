// Tabulate votes for non-eliminated candidates
void tabulate(void)
{
    for (int i = 0; i < voter_count; i++)
    {
        for (int j = 0; j < candidate_count; j++)
        {
            for (int h = 0; h < candidate_count; h++)
            {
                if (preferences[i][j] == h)
                {
                    if (candidates[h].eliminated == false)
                    {
                        candidates[h].votes++;
                    }
                    else
                    {
                        /* code */
                    }
                    
                }
            }
        }
    }

        for (int h = 0; h < candidate_count; h++)
    {
        if (candidates[h].eliminated == false)
        {
            for (int i = 0; i < voter_count; i++)
            {
                for (int j = 0; j < candidate_count; j++)
                {
                    if (preferences[i][j] == h)
                    {
                        candidates[h].votes++;
                    }
                }
            }
        }
        else
        {
            /* code */
        }